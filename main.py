import re
import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.core.window import Window
from pathlib import Path

from video_parser import VideoParser

# 设置窗口大小（模拟手机屏幕）
Window.size = (360, 640)
Window.clearcolor = (0.05, 0.05, 0.05, 1)  # 深色背景


class ModernButton(Button):
    """自定义按钮样式"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(48)
        self.font_size = dp(16)
        self.bold = True
        self.color = (1, 1, 1, 1)
        self.background_color = (0.2, 0.6, 0.9, 1)
        self.border_radius = [dp(8)]


class DownloadItem(BoxLayout):
    """单个下载任务 UI"""
    def __init__(self, url, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(140)
        self.padding = dp(10)
        self.spacing = dp(6)
        self.canvas.before.clear()

        with self.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(0.15, 0.15, 0.15, 0.9)
            self.rounded_rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(12), dp(12), dp(12), dp(12)]
            )

        self.url = url
        self.parser = VideoParser()

        # 标题
        self.title_label = Label(
            text="准备解析...",
            size_hint_y=None,
            height=dp(35),
            halign='left',
            valign='middle',
            font_size=dp(14),
            color=(1, 1, 1, 1),
            padding=(dp(5), 0)
        )
        self.title_label.bind(
            width=lambda *x: setattr(self.title_label, 'text_size', (self.title_label.width, None))
        )
        self.add_widget(self.title_label)

        # 进度条
        self.progress = ProgressBar(
            max=100,
            size_hint_y=None,
            height=dp(20),
            color=(0.2, 0.8, 0.5, 1)
        )
        self.add_widget(self.progress)

        # 状态标签
        self.status_label = Label(
            text="等待开始",
            size_hint_y=None,
            height=dp(25),
            font_size=dp(11),
            color=(0.7, 0.7, 0.7, 1)
        )
        self.add_widget(self.status_label)

        # 开始下载
        Clock.schedule_once(lambda dt: self.start_download(), 0.5)

    def start_download(self):
        def _run():
            result = self.parser.parse_and_download(self.url, progress_callback=self.on_progress)
            Clock.schedule_once(lambda dt: self.on_complete(result), 0)

        threading.Thread(target=_run, daemon=True).start()

    def on_progress(self, percent, status):
        Clock.schedule_once(lambda dt: self._update_progress(percent, status), 0)

    def _update_progress(self, percent, status):
        self.progress.value = percent
        self.status_label.text = status

    def on_complete(self, result):
        if result.get('success'):
            self.title_label.text = result.get('title', '完成')[:50]
            self.status_label.text = f"✅ 已保存: {result.get('filename', '')}"
            self.progress.value = 100
        else:
            self.title_label.text = "❌ 解析失败"
            self.status_label.text = result.get('error', '未知错误')[:50]


class VideoParserApp(App):
    def __init__(self):
        super().__init__()
        self.parser = VideoParser()

    def build(self):
        self.title = "视频解析下载"
        root = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(12))

        # 标题区域
        title_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(60))
        title = Label(
            text='🎬 视频解析下载',
            size_hint_y=None,
            height=dp(40),
            font_size=dp(22),
            bold=True,
            color=(1, 0.8, 0.2, 1)  # 金色标题
        )
        title_layout.add_widget(title)

        subtitle = Label(
            text='支持抖音/快手/小红书/B站/视频号/YouTube/TikTok',
            size_hint_y=None,
            height=dp(20),
            font_size=dp(10),
            color=(0.6, 0.6, 0.6, 1)
        )
        title_layout.add_widget(subtitle)
        root.add_widget(title_layout)

        # 输入区域
        input_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(120), spacing=dp(8))

        # 输入框
        self.url_input = TextInput(
            hint_text='粘贴分享文本或视频链接...',
            multiline=True,
            size_hint_y=None,
            height=dp(60),
            font_size=dp(14),
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            padding=(dp(10), dp(10))
        )
        input_layout.add_widget(self.url_input)

        # 按钮行
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(48), spacing=dp(8))

        extract_btn = ModernButton(text='🔗 提取链接', size_hint_x=0.4, on_press=self.extract_url)
        extract_btn.bind(on_release=lambda x: setattr(extract_btn, 'background_color', (0.2, 0.7, 0.8, 1)))
        btn_layout.add_widget(extract_btn)

        parse_btn = ModernButton(text='▶ 解析下载', size_hint_x=0.6, on_press=self.start_parse)
        parse_btn.background_color = (0.2, 0.8, 0.5, 1)  # 绿色
        btn_layout.add_widget(parse_btn)

        input_layout.add_widget(btn_layout)
        root.add_widget(input_layout)

        # 下载列表标题
        list_title = Label(
            text='📥 下载列表',
            size_hint_y=None,
            height=dp(30),
            font_size=dp(16),
            bold=True,
            halign='left',
            color=(1, 1, 1, 1)
        )
        root.add_widget(list_title)

        # 下载列表
        scroll = ScrollView(size_hint_y=0.6)
        self.download_list = GridLayout(cols=1, spacing=dp(8), size_hint_y=None)
        self.download_list.bind(minimum_height=self.download_list.setter('height'))
        scroll.add_widget(self.download_list)
        root.add_widget(scroll)

        # 底部信息
        info = Label(
            text='v1.0.0 | 仅供个人学习使用',
            size_hint_y=None,
            height=dp(25),
            font_size=dp(9),
            color=(0.4, 0.4, 0.4, 1)
        )
        root.add_widget(info)

        return root

    def extract_url(self, instance):
        """从分享文本中提取链接"""
        text = self.url_input.text.strip()
        if not text:
            self.show_popup("提示", "请先粘贴分享文本")
            return

        url = self.parser.extract_url_from_text(text)
        if url:
            self.url_input.text = url
            platform = self.parser.identify_platform(url)
            self.show_popup("✅ 提取成功", f"平台: {platform}\n链接: {url[:60]}...")
        else:
            self.show_popup("❌ 未找到链接", "未在文本中检测到视频链接")

    def start_parse(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.show_popup("提示", "请输入链接")
            return

        # 添加下载项
        item = DownloadItem(url=url)
        self.download_list.add_widget(item)
        self.url_input.text = ''

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        content.add_widget(Label(text=message, halign='center', valign='middle', color=(1, 1, 1, 1)))
        btn = ModernButton(text='确定', size_hint_y=None, height=dp(40))
        content.add_widget(btn)
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.85, 0.35),
            background_color=(0.1, 0.1, 0.1, 0.9)
        )
        btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    VideoParserApp().run()
