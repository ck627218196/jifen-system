<template>
  <div >
    <Header></Header>
    <el-container style="height:1000px">
      <el-aside class="aside">
        <div class="menu1">不参加考核人员录入</div>
        <div class="menu2">部门月考核成绩录入</div>
        <div class="menu3">经理月绩效打分</div>
        <!--        <div class="menu4">小ceo月绩效打分</div>-->
        <div class="menu5">其他积分录入</div>
        <div class="menu6">员工月积分导出</div>
      </el-aside>

      <el-container>


        <el-main>
<!--          提示栏-->
          <div class="tip">
            提示：<br/>
            1.输入KPI考核的分数并点击提交即可<br/>
            2.请务必在&nbsp;20&nbsp;日之前完成提交，过时则无法完成操作！
          </div>
          <!--          <div ><p>当前时间：{{nowTime}}</p></div>-->

<!--          表格部分-->
          <div class="main-table">
            <el-table :data="tableData" border style="width: 100%" :cell-style="cellstyle">
              <el-table-column prop="bumen" label="部门" min-width="80%" align="center" ></el-table-column>
              <!-- <el-table-column prop="name" label="姓名" width="270"></el-table-column> -->
              <el-table-column prop="time" label="考核月份" min-width="80%" align="center" ></el-table-column>
              <el-table-column prop="dafen" label="考核分数" align="center" min-width="90%">
                <template slot-scope="scope">
                  <el-input v-model="scope.row.dafen"></el-input>
                </template>
              </el-table-column>
            </el-table>
<!--            操作按钮-->
            <div class="submit-button">
              <el-button type="primary" @click="submitForm('numberValidateForm')">提交</el-button>
              <el-button @click="previousdata">查看以往数据</el-button>
            </div>
          </div>

        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
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
    background-color: rgb(66, 75, 87);
    color: aliceblue;
  }

  .menu3 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
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
  import Header from "./some_components/Header"
  export default {
    components:{
      Header,
    },
    data() {
      return {
        loading: true,
        date: '',
        lastdate:"",
        tableData: [{
          bumen: '2I业务营销中心',
          time: '',
          dafen: ''
        }, {
          bumen: '商城营销中心',
          time: '',
          dafen: ''
        }, {
          bumen: '互联网合作平台营销中心',
          time: '',
          dafen: ''
        }, {
          bumen: '连锁渠道营销中心',
          time: '',
          dafen: ''
        }, {
          bumen: '互联网流量运营中心',
          time: '',
          dafen: ''
        }, {
          bumen: '数据分析应用中心',
          time: '',
          dafen: ''
        }, {
          bumen: '互联网系统运营中心',
          time: '',
          dafen: ''
        }, {
          bumen: '订单运营中心',
          time: '',
          dafen: ''
        }, {
          bumen: '资源支撑运营中心',
          time: '',
          dafen: ''
        }, {
          bumen: '互联网服务体验中心',
          time: '',
          dafen: ''
        }, {
          bumen: '经营监控中心',
          time: '',
          dafen: ''
        }, {
          bumen: '党政综合管理部',
          time: '',
          dafen: ''
        }]
      }
    },
    methods: {
      // 跳转查看已录入数据
      previousdata(){
        this.$router.push({name:"assessdata"});
      },
// 表格内字体样式
      cellstyle() {
        return 'text-align: center'
      },

      kpiopenreceive(){
        this.$axios.get('api/kpiopenreceive/')
          .then(response=>{
            if(response.data.num === 0){
              this.lastdate = response.data.data
              this.nowTimes();
            }else(
              this.$message.error('系统错误')
            )
          })
      },

      submitForm(formName) {
        this.$confirm('此操作将提交各部门考核成绩, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          customClass: 'confirmbox1',
          type: 'warning'
        }).then(() => {
          this.$axios.post('api/assess/', {
            tableData: this.tableData
          }).then(res => {
            if (res.data.num === "1") {
              this.$message({
                type: 'success',
                message: '提交成功!'
              });
            } else if (res.data.num === "2") {
              this.$message({
                type: 'error',
                message: '填写不完整!'
              });
            }
          }).catch(() => {
            this.$message({
              type: 'error',
              message: '提交失败'
            });
          })
          // this.$message({
          //   type: 'success',
          //   message: '提交成功!'
          // });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消提交'
          });
        });
      },
      // 根据时间判断当前是否可登录
      timeFormate(timeStamp) {
        let year = new Date(timeStamp).getFullYear();
        let month = new Date(timeStamp).getMonth() + 1 < 10 ? "0" + (new Date(timeStamp).getMonth() + 1) : new Date(timeStamp).getMonth() + 1;
        let date = new Date(timeStamp).getDate() < 10 ? "0" + new Date(timeStamp).getDate() : new Date(timeStamp).getDate();
        let hh = new Date(timeStamp).getHours() < 10 ? "0" + new Date(timeStamp).getHours() : new Date(timeStamp).getHours();
        let mm = new Date(timeStamp).getMinutes() < 10 ? "0" + new Date(timeStamp).getMinutes() : new Date(timeStamp).getMinutes();
        // let ss =new Date(timeStamp).getSeconds() < 10? "0" + new Date(timeStamp).getSeconds(): new Date(timeStamp).getSeconds();
        // return year + "年" + month + "月" + date +"日"+" "+hh+":"+mm ;
        // this.nowTime = year + "年" + month + "月" + date + "日" + " " + hh + ":" + mm;
        // this.DATE = date;
        // console.log(this.nowTime);
        if (date>this.lastdate) {
          this.$alert('人员录入时间已超过，请联系人力资源负责人', '提示', {
            confirmButtonText: '确定',
            callback: action => {
              this.$router.push({name: "login3"})
            }
          });
        } else {
          console.log(111)
        }
      },
      // 执行时间判断函数
      nowTimes() {
        this.timeFormate(new Date());
        // setInterval(this.nowTimes, 30 * 1000);
      }
    },

    // getid(){
    //       console.log(this.$route)
    //   },
    created() {
      this.kpiopenreceive();
      this.$axios.get("api/status/")
        .then(response => {
          if (response.data.first_name === "11") {
            this.loading = false;
            this.$axios.get('api/assessmonth/')
              .then(response => {
                for (let i of this.tableData) {
                  this.$set(i, 'time', response.data.data)
                  // 给time属性赋值
                }
                // this.$set(this.tableData[0,1,2,3,4,5,6,7,8,9,10,11],'time',response.data.data)
              })
          } else {
            this.$router.push({name: "login3"})

          }
        })
    },
    mounted() {
    },
  }
</script>
