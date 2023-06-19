<template>
  <div class="header">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
      <el-menu-item index="0"><h1>CNN-TEST</h1></el-menu-item>
      <div class="flex-grow" />
      <!-- <div class="page"> -->
        <el-menu-item index="1">实验过程</el-menu-item>
        <el-menu-item index="2" style="margin-right: 2%;">应用</el-menu-item>
    <!-- </div> -->
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style>
.header{
  background-color: aliceblue;
  background: fixed;
  background: #a1e9d2;
}
.flex-grow {
  flex-grow: 1;
  background-color: rgb(254, 254, 254);
}
.page{
  position: relative;
  display: flex;
  margin-right: 20px;
}
</style>
