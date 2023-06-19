import MarkdownIt from 'markdown-it';
import markdownItHighlightjs from 'markdown-it-highlightjs';

// 创建 Markdown 实例
const md = new MarkdownIt({
    html: true, // 启用 HTML 标签解析
});

// 添加 markdown-it-highlightjs 插件
md.use(markdownItHighlightjs);