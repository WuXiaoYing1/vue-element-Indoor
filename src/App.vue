  <script setup>
import { RouterLink, RouterView } from 'vue-router'
import { requiredNumber } from 'element-plus/es/components/table-v2/src/common';
import { ElContainer,ElAside,ElHeader,ElMain } from 'element-plus';
import Head from './components/Head.vue'
import Down from './views/Down.vue'
</script>

<template>
    <el-container class="Container">
      <el-header class="common-layout">
        <div class="header">
          <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            :ellipsis="false"
            @select="handleSelect"
          >
            <el-menu-item index="0">CNN-TEST</el-menu-item>
            <div class="flex-grow" />
            <div class="page">
              <a href="#/"><el-menu-item index="1">实验过程</el-menu-item></a>
              <a href="#/using"><el-menu-item index="2" style="margin-right: 2%;">应用</el-menu-item></a>
              </div>
            </el-menu>
        </div>
      </el-header>
      <el-main class="mainer1">
        <component :is="currentView" />
      </el-main>
    </el-container>
</template>

<script>
import Down from './views/Down.vue';
import Using from './views/Using.vue';
const routes = {
  '/': Down,
  '/using': Using,
}
export default {
    data() {
        return {
        currentPath: window.location.hash
    }
    },
  components: {
    ElContainer,
    Head,
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/']
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
		  this.currentPath = window.location.hash
		})
  }
}
</script>

<style scoped>
el-container{
  width: 100%;
  height: 100%;
}

el-main{
  margin: auto;
}
.common-layout{
  margin-left: -1rem;
  /* margin: ; */
}
.Container{
  
}
/* .logo{
  display: flex;
} */
.header {
  /* margin-left: 10%; */
  /* margin-left: -11rem; */
  width: 100%;
  position: fixed;
  /* display: flex; */
}
.asider{
  margin-top: 50px;
  min-width: 100px;
  /* height: 100%; */
}
.mainer1{
  height: 200%;
  width: 100%;
  margin: auto;
  align-items: center;
  position: relative;
}
.downer{
  margin-top: 50%;
}
.common-layout{
  border: 10px;
}
a{
  text-decoration:none;
color:#333;
}
.flex-grow {
  flex-grow: 1;
}
.page{
  display: flex;
  margin-right: 2%;
}
nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}
.but1{
  position: relative;
  margin:auto;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
