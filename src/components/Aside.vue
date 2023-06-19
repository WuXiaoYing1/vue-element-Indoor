<template>
      <div class="article-directory aside-size">
            <span>目录</span>
            <div v-for="(heading, i) in tocs" :key="i + ''" class="catalog-item" :style="{ padding: `10px 0 10px ${(Number(heading[1])-1) * 10}px` }">
              </div>
          </div>
  </template>
  

<script>
import MarkdownIt from 'markdown-it'
import MarkdownItAnchor from 'markdown-it-anchor'
import uslug from 'uslug'
import MarkdownItTocDoneRight from 'markdown-it-toc-done-right';


export default {
  data() {
    return {
      tocs: '',
    }
  },
  async created() {
    const md = new MarkdownIt().use(MarkdownItTocDoneRight, {
      level: 3,
      containerHeaderHtml: '<strong>Table of Contents</strong>',
      containerClass: 'custom-toc',
      linkClass: 'custom-toc-link'
    });
    // const tocContainer = document.getElementById('toc-container');
    const response = await fetch('../../public/状态机.md');
    const markdown = await response.text();
    const result = md.render(markdown);
    const lines = result.split('\n')
    const regex = /<h([1-6])\s+id="([^"]+)"[^>]*>(.+?)<\/h\1>/gi
    const toc = []
    for (let i = 0; i < lines.length; i++) {
      toc[i] = regex.exec(lines[i])
    }
    this.tocs = toc.filter(line => line !== null)
  },
};
</script>
<style>
    .tac{
        min-width: 100px;
        height: 100%;
        /* display: flex; */
    }

</style>
  

