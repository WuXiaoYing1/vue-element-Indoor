<template>
  <el-container class="contain">
    <el-main class="mainer">
    <div class="shadow">
    <div class="all">
      <div>
      <h2>文件上传</h2>
      <input type="file" ref="fileInput" @change="handleFileChange">
      </div>
      <button @click="identify" style="margin-top: 1%;">分类</button>
      <div class="imgss">
        <img :src="imgs"  style="max-width: 300px;max-height: 300px;">
    </div>
    <div class="anss">
        <span>{{ ans }}</span>
    </div>
    </div>
    </div>
  </el-main>
  </el-container>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      selectedFile: null,
      imgs:'',
      ans:'',
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(this.selectedFile);
      reader.onload = () => {
        this.imgs = reader.result;
      };
      this.ans=''
    },
    async sent() {
      const formData = new FormData();
      const response = await axios.get('/api/sent')
      console.log(response.data)
    },
    async identify() {
      const formData = new FormData();
      formData.append("file", this.selectedFile);
      const response = await axios.post('/api/identify', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      console.log(response.data)
        this.ans='它的分类是'+response.data
        
    }
  }
};
</script>

<style>
.mainer{
  /* position: relative;
  display: inline-flex;
  justify-content: center;
  align-items: center; */
  margin: auto;
  height: 100%;
}
.contain{
  margin: auto;
  height: 100%;
  position: relative;
  display: inline-flex;
  justify-content: center;
  align-items: center;

}
.all{
  width: 90%;
  height: 10%;
  margin: auto;
}
.imgss{
  max-width: 300px;
  max-height: 300px;
}
.shadow{
  margin: auto;
  margin-top: 10%;
  width: 30%;
  box-shadow: 0 0 3px 3px #ccc;
}
</style>