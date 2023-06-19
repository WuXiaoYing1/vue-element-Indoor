
<script setup>
import Main from '../components/Main.vue'
import Aside from '../components/Aside.vue'
import { ElContainer, ElAside, ElHeader, ElMain } from 'element-plus';

</script>

<template>
    <el-container class="tac">
        <el-aside class="sider">
            <Aside/>
        </el-aside>
        <el-main class="mainer">
            <Main/>
        </el-main>
    </el-container>
</template>

<style>
.tac{
    position: relative;
}

.mainer{
    height: 100%;
    width: 100%;
    /* margin: auto; */
    /* position: relative; */
}

.sider{
    /* background: lightgray; */
            /* padding: 0;
            bottom: 0; */
    /* width: 10px; */
    max-width: 30px;
}
</style>





