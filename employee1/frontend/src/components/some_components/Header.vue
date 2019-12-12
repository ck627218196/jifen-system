<template>
  <div class="conTainer">
    <el-header style="height:100px;" class="header headerBar" >
      <span>电商积分管理系统</span>
    </el-header>
  </div>
</template>

<script>
    export default {
        name: "header"
    }
</script>

<style scoped>
  .headerBar{
      position: fixed;
      top: 0;
      z-index: 999;
      width:100%;
  }
  .conTainer{
    height: 100px;
  }
  .header {
    background-color: rgb(66, 75, 87);
    color: white;
    text-align: center;
    font-size: 30px;
    height:100px;
    line-height:95px;
  }
</style>
