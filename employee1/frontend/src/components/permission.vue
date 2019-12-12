<template>
  <div >
    <Header></Header>
    <el-container style="height:1000px">
      <el-aside class="aside">
        <div class="menu1"></div>
        <div class="menu2"></div>
        <div class="menu3">权限管理</div>
        <!--        <div class="menu4">小ceo月绩效打分</div>-->
        <div class="menu5"></div>
        <div class="menu6"></div>
      </el-aside>

      <el-container>


        <el-main>
          <div class="tip">
            提示：<br/>
            1.点击开启按钮即可解除所对应账户的登录时间限制<br/>
            2.点击重置按钮即可恢复默认的登录截至日期。
          </div>
          <!--          <div ><p>当前时间：{{nowTime}}</p></div>-->
          <div class="main-table">
            <el-table :data="tableData" border style="width: 100%" :cell-style="cellstyle">
              <el-table-column prop="bumen" label="系统账号" min-width="80%" align="center" ></el-table-column>
              <!-- <el-table-column prop="name" label="姓名" width="270"></el-table-column> -->
              <el-table-column prop="time" label="开启账号" min-width="80%" align="center">
                <template slot-scope="scope">
                  <el-button size="small" @click="handleopen(scope.$index,scope.row)">开启</el-button>
                </template>

              </el-table-column>
              <el-table-column prop="dafen" label="重置账号" align="center" min-width="90%">
                <template slot-scope="scope">
                  <el-button size="small" @click="handlereset(scope.$index,scope.row)">重置</el-button>
                </template>
              </el-table-column>
            </el-table>
            <div class="submit-button">
            </div>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
  .el-header {
    background-color: rgb(66, 75, 87);
    color: white;
    text-align: center;
    font-size: 30px;
    height:100px;
    line-height:95px
  }

  .aside {
    color: #333;
    width: 300px
  }

  .tip {
    color: red;
    font-size: 25px;
    margin-left: 120px;
  }

  .main-table {
    margin-left: 120px;
    margin-top: 20px;
    width: 75%;
  }

  .submit-button {
    margin-top: 30px;
    margin-left: 350px
  }

  .el-input {
    height: 40px;
    font-size: 20px
  }

  .el-table {
    font-size: 20px
  }

  .menu1 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    margin-top: 10px;
    border: 1px solid #eee
  }

  .menu2 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
    /* background-color: rgb(66, 75, 87);
    color: aliceblue; */
  }

  .menu3 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
    background-color: rgb(66, 75, 87);
    color: aliceblue;
  }

  /*.menu4 {*/
  /*  height: 100px;*/
  /*  width: 290px;*/
  /*  font-size: 22px;*/
  /*  text-align: center;*/
  /*  line-height: 100px;*/
  /*  border: 1px solid #eee*/
  /*}*/

  .menu5 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }

  .menu6 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }
@media screen and (max-width: 768px){

  .header .el-header{
    background-color: rgb(66, 75, 87);
    color: white;
    text-align: center;
    font-size: 30px;
    height:100px;
    line-height:95px
  }
  .aside{
    color: #333;
    width: 0px!important
  }
  .main-table {
    margin-left: 10px;
    margin-top: 20px;
    width: 100%;
  }
  .el-table {
    font-size: 12px;
    width: 100%;
  }
  .tip {
    color: red;
    font-size: 15px;
    margin: 5px 0px 10px 5px;
    line-height: 20px;
  }
   .el-input {
    font-size: 14px!important;
  }
  .submit-button {
    margin-top: 30px;
    margin-left: 40%
  }
  .menu1 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    margin-top: 10px;
    border: 1px solid #eee
  }

  .menu2 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
    background-color: rgb(66, 75, 87);
    color: aliceblue;
  }

  .menu3 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }

  .menu5 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }

  .menu6 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }
}
</style>
<style>
.el-message-box, .confirmbox1{
    width: 350px
  }
</style>
<script>
  import Header from "./some_components/Header.vue"
  export default {
    data() {
      return {
        lastdate:"31",
        lastdate1:"20",
        lastdate2:"27",
        loading: true,
        date: '',
        tableData: [{
          bumen: 'kpi录入',
          time: '',
          dafen: ''
        }, {
          bumen: '经理打分',
          time: '',
          dafen: ''
        }]
      }
    },
    methods: {
      cellstyle() {
        return 'text-align: center'
      },

      handlereset(row){
        if(row === 0){
          // 重置kpi录入账号的登录截至时间
          this.$confirm('此操作将开放kpi录入者的登录权限, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(()=>{
          this.$axios.post('api/kpiuserreset/',{
            lastdate1: this.lastdate1
          }).then(res=>{
            if (res.data.num === "1"){
              this.$message({
                  type: 'success',
                  dangerouslyUseHTMLString: true,
                  message: '<div style="font-size: 20px">操作成功！</div>'
                });
            }else{
              this.$message({
                type: 'info',
                message: '操作失败!'
              });
            }
          })
          }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消操作'
          });
        })

        }else if(row === 1){
          // 重置经理打分账号的登陆截至时间
          this.$confirm('此操作将开放kpi录入者的登录权限, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(()=>{
          this.$axios.post('api/manageruserreset/',{
            lastdate2: this.lastdate2
          }).then(res=>{
            if (res.data.num === "1"){
              this.$message({
                  type: 'success',
                  dangerouslyUseHTMLString: true,
                  message: '<div style="font-size: 20px">操作成功！</div>'
                });
            }else{
              this.$message({
                type: 'info',
                message: '操作失败!'
              });
            }
          })
          }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消操作'
          });
        })
        }
      },

      handleopen(row){
        console.log(row)
        if(row === 0){
          // 对kpi考核账号的权限管理
      this.$confirm('此操作将开放kpi录入者的登录权限, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
            this.$axios.post('api/kpiuseropen/',{
              lastdate: this.lastdate
            }).then(res=>{
              if (res.data.num === "1") {
                this.$message({
                  type: 'success',
                  dangerouslyUseHTMLString: true,
                  message: '<div style="font-size: 20px">操作成功！</div>'
                });
              }else{
                this.$message({
                type: 'info',
                message: '操作失败!'
              });
              }
            })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消操作'
          });
        })

        }else if(row === 1){
          // 对经理打分账号的权限管理
          this.$confirm('此操作将开放各位经理的登录权限, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
            this.$axios.post('api/manageruseropen/',{
              lastdate: this.lastdate
            }).then(res=>{
              if (res.data.num === "1") {
                this.$message({
                  type: 'success',
                  dangerouslyUseHTMLString: true,
                  message: '<div style="font-size: 20px">操作成功！</div>'
                });
              }else{
                this.$message({
                type: 'info',
                message: '操作失败!'
              });
              }
            })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消操作'
          });
        })
        }
    }
    },

    // getid(){
    //       console.log(this.$route)
    //   },
    created() {
      this.$axios.get("api/status/")
        .then(response => {
          if (response.data.first_name === "66") {
            this.loading = false;
          } else {
            this.$router.push({name: "login3"})

          }
        })
    },
    mounted() {
    },
  }
</script>
