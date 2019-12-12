<template>
  <div>
    <Header></Header>
    <el-container style="height:1000px" class="container1">
      <el-aside class="aside">
        <div class="menu1">不参加考核人员录入</div>
        <div class="menu2">部门月考核成绩录入</div>
        <div class="menu3">经理月绩效打分</div>
        <!--        <div class="menu4">小ceo月绩效打分</div>-->
        <div class="menu5">其他积分录入</div>
        <div class="menu6">员工月积分导出</div>
      </el-aside>

      <el-container>
        <!-- <div class="tip">{{msg}}</div> -->
        <el-main>
          <div class="tip">
            提示：<br/>
            1.您部门本月的KPI成绩为&nbsp;{{msg1}}&nbsp;分，组内排名为第&nbsp;{{msg2}}&nbsp;名。本月参与考核员工为&nbsp;{{msg3}}&nbsp;名。<br/>
            2.您部门本月得A为&nbsp;{{msg4}}&nbsp;名，B+为&nbsp;{{msg5}}&nbsp;名，B+C+D一共为&nbsp;{{msg6}}&nbsp;名，其中c+d人数大于等于&nbsp;{{msg7}}&nbsp;。<br/>
            3.请务必在&nbsp;27&nbsp;日之前完成提交，过时则无法完成操作！
          </div>
          <el-table :data="tableData">
            <el-table-column prop="jobnum" label="工号" min-width="50%"></el-table-column>
            <el-table-column prop="name" label="姓名" min-width="50%"></el-table-column>
            <el-table-column prop="department" label="部门" min-width="60%"></el-table-column>
            <el-table-column prop="time" label="月份" min-width="40%"></el-table-column>
            <!-- <el-table-column prop="dafen" label="打分" min-width="80%">
              <template slot-scope="scope">
                <el-input v-model="scope.row.dafen" placeholder=""></el-input>
              </template>
            </el-table-column> -->
            <el-table-column prop="level" label="考核等级" min-width="80%">
              <template slot-scope="scope">
                <el-select v-model="scope.row.level" placeholder="等级">
                  <el-option label="A" value="A"></el-option>
                  <el-option label="B+" value="B+"></el-option>
                  <el-option label="B" value="B"></el-option>
                  <el-option label="C" value="C"></el-option>
                  <el-option label="D" value="D"></el-option>
                </el-select>
              </template>
            </el-table-column>
          </el-table>
          <div class="submit-button">
            <el-button type="primary" @click="submitForm('numberValidateForm')">提交</el-button>
            <el-button @click="previousdata">查看以往数据</el-button>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  import Header from "./some_components/Header.vue";
  export default {
    components:{
      Header,
    },
    data() {
      return {
        lastdate:2,
        msg1: '',
        msg2: '',
        msg3: '',
        msg4: '',
        msg5: '',
        msg6: '',
        msg7: '',
        tableData: [
          {
            jobnum: "",
            department:"",
            name: "",
            time: "",
            // dafen: "",
            level: ""
          }
        ]
      };
    },
    methods: {
          // 查看已录入数据
      previousdata(){
        this.$router.push({name:"managermarkdata"});
      },

      manageropenreceive(){
        this.$axios.get('api/manageropenreceive/')
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
        this.$confirm('即将提交本部门员工考核成绩, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          customClass: 'confirmbox',
          type: 'warning'
        }).then(() => {
          this.$axios.post('api/managermark/', {
            tableData: this.tableData,
            msg2: this.msg2,
            msg3: this.msg3,
            msg4: this.msg4,
            msg5: this.msg5,
            msg6: this.msg6,
            msg7: this.msg7,
          }).then(res => {
            if (res.data.num === "1") {
              this.$message({
                type: 'success',
                dangerouslyUseHTMLString: true,
                message: '<div style="font-size: 20px">提交成功！</div>'
              });
            } else if (res.data.num === "2") {
              this.$message({
                type: 'error',
                dangerouslyUseHTMLString: true,
                message: '<div style="font-size: 20px">您所提交的评级数量错误</div>'
              });
            } else if (res.data.num === "3") {
              this.$message({
                type: 'error',
                dangerouslyUseHTMLString: true,
                message: '<div style="font-size: 20px">您有空白项未填写</div>'
              });
            } else {
              this.$message({
                type: 'info',
                message: '提交失败!'
              });
            }
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

      timeFormate(timeStamp) {
        let year = new Date(timeStamp).getFullYear();
        let month = new Date(timeStamp).getMonth() + 1 < 10 ? "0" + (new Date(timeStamp).getMonth() + 1) : new Date(timeStamp).getMonth() + 1;
        var date = new Date(timeStamp).getDate() < 10 ? "0" + new Date(timeStamp).getDate() : new Date(timeStamp).getDate();
        let hh = new Date(timeStamp).getHours() < 10 ? "0" + new Date(timeStamp).getHours() : new Date(timeStamp).getHours();
        let mm = new Date(timeStamp).getMinutes() < 10 ? "0" + new Date(timeStamp).getMinutes() : new Date(timeStamp).getMinutes();
        // let ss =new Date(timeStamp).getSeconds() < 10? "0" + new Date(timeStamp).getSeconds(): new Date(timeStamp).getSeconds();
        // return year + "年" + month + "月" + date +"日"+" "+hh+":"+mm ;
        // this.nowTime = year + "年" + month + "月" + date + "日" + " " + hh + ":" + mm;
        // console.log(this.nowTime);
        // this.DATE = date;
        console.log(this.lastdate+'天');
        if (date > this.lastdate) {
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

      nowTimes() {
        this.timeFormate(new Date());
        // setInterval(this.nowTimes, 30 * 1000);
      }

    },
    created() {
      this.manageropenreceive();
      this.$axios.get('api/status/')
        .then(response => {
          if (response.data.first_name === "44") {
            this.loading = false;
            this.$axios.get('api/compute/')
              .then(response => {
                if (response.data.num === "0") {
                  this.$alert('当前时段不可操作，请等待人员录入与kpi录入后再登陆', '提示', {
                    confirmButtonText: '确定',
                    callback: action => {
                      this.$router.push({name: "login3"})
                    }
                  });
                } else {
                  var rr = response.data.data
                  this.msg1 = rr['kpi']
                  this.msg2 = rr['rank']
                  this.msg3 = rr['person']
                  this.msg4 = rr['A']
                  this.msg5 = rr['B+']
                  this.msg6 = rr['B+C+D']
                  this.msg7 = rr['C+D']
                }
              })

            this.$axios.get('api/markname/')
              .then(response => {
                if (response.data.num === "1") {
                  this.$alert('当前时段不可操作，请等待人员录入与kpi录入后再登陆', '提示', {
                    confirmButtonText: '确定',
                    callback: action => {
                      this.$router.push({name: "login3"})
                    }
                  });
                } else {
                  this.tableData = response.data.data
                }
              })
            // this.$router.push({name:"login3"})

          } else {
            this.$router.push({name: "login3"})

            // 获取users
            // this.$axios.get('apis/get_info?users=2ds2ppJu2I9dl1&aa=32&kk=34')
            //   .then(response => {
            //     this.users = response.data.data
            //     this.loading = false
            //   }, error => {
            //     console.log(error)
            //   })

          }
        })
    },
    mounted() {

      // this.nowTimes();
    },
  }
</script>

<style scoped>
  /*.el-header {*/
  /*  background-color: rgb(66, 75, 87);*/
  /*  color: white;*/
  /*  text-align: center;*/
  /*  font-size: 30px;*/
  /*  height:100px;*/
  /*  line-height:95px*/
  /*}*/

  .submit-button {
    margin-top: 30px;
    margin-left: 350px;
  }

  .aside {
    color: #333;
    width: 200px
  }

  .el-main {
    font-size: 20px;
    margin-left: 120px;
    padding: 10px;
  }

  .el-table {
    font-size: 20px;
    width: 80%;
  }

  .el-input__inner {
    font-size: 20px;
    padding-left:10px!important
  }

  .el-input {
    height: 40px;
    font-size: 20px;
  }

  .tip {
    color: red;
    font-size: 25px;
    margin: 0px 50px 10px 0px;
    line-height: 40px;
  }

  .menu1 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    margin-top: 10px;
    border: 1px solid #eee;
  }

  .menu2 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
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
  /*  border: 1px solid #eee;*/
  /*}*/
  .menu5 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
  }

  .menu6 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
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
  .el-main {
    font-size: 12px;
    margin-left: 0px;
    padding: 0px;
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
    font-size: 12px!important;
  }
  .el-input__inner {
    font-size: 10px;
    padding:0 10px!important
  }
  .submit-button {
    margin-top: 30px;
    margin-left: 40%;
  }


  .menu1 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    margin-top: 10px;
    border: 1px solid #eee;
  }

  .menu2 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
  }

  .menu3 {
    height: 100px;
    width: 0px;
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
  /*  border: 1px solid #eee;*/
  /*}*/
  .menu5 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
  }

  .menu6 {
    height: 100px;
    width: 0px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
  }
  /* .el-message-box{
    max-width: 420px
  } */
}
/* } */
</style>
<style>
.el-message-box, .confirmbox{
    width: 350px
  }
</style>

