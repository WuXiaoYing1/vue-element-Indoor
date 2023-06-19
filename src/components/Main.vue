<template>
    <div class="process">
        <div class="content">
        <div class="markdown-body" v-html="html"></div>
        </div>
    </div>
  </template>
  
  <script>
  import Markdown from 'markdown-it';
  import hljs from 'highlight.js';
  import 'github-markdown-css/github-markdown.css';
  const md = new Markdown({
      html: true,
      xhtmlOut: false, // 使用 '/' 自闭标签（比如 <br />），而不是纯 HTML5 格式（比如 <br>）
      breaks: false, // 转换段落里的 '\n' 到 <br>。
      langPrefix: 'language-', // CSS 类名前缀，默认值是 'language-'。
      linkify: true, // 自动转换链接。
      typographer: true, // 启用一些语言相关的替换 + 引号美化。
      quotes: '“”‘’'
    })
  export default {
    data() {
      return {
        markdown: '',
        html: '',
      };
    },
    async created() {
      // 异步加载 Markdown 文件并读取其中的内容
      const response = await fetch('../../public/状态机.md');
      this.markdown = await response.text();
      // 解析 Markdown 代码，并进行代码块的高亮
      const result = md.render(this.markdown);
      this.html = this.highlightCode(result);
    },
    methods: {
      highlightCode(html) {
        const codeBlock = /<pre><code(?:\sclass="([\w-]+)")?>([\s\S]+?)<\/code><\/pre>/g;
        html = html.replace(codeBlock, (match, lang, code) => {
          if (lang && hljs.getLanguage(lang)) {
            try {
              code = hljs.highlight(code, { language: lang }).value;
            } catch (__) {
              // 高亮失败，使用原始代码
            }
          } else {
            code = hljs.highlightAuto(code).value;
          }
          return `<pre><code class="hljs ${lang}">${code}</code></pre>`;
        });
        return html;
      },
    },
  };
  </script>
  
  <style>
  .hljs{
    /* background-color: rgb(248, 245, 245); */
    max-width: 500px;
  }
  h1{
    font-size: 32px;
  }
  .process{
        /* box-shadow: 0 0 5px 1px #998; */
        margin: auto;
        /* margin-right: 20%; */
        min-width: 500px;
        width: 800px;
        max-width:1500px;
        /* height: 150%;  */
        /* overflow: hidden; */
        /* margin-bottom: 1%; */
        position: relative;
    }
    .content{
        margin-left: 1%;
        height: 200%; /* 继承.box高度 */
        /* background: -webkit-linear-gradient(top, transparent 40px, rgb(21, 21, 21) 41px),-webkit-linear-gradient(left, transparent 40px, rgb(12, 12, 12) 41px); */
        background-size: 41px 41px;
        /* overflow-y:visible; */
    }
    /* .pre{
      width: 700px;
    } */
  </style>
  