<template>
  <div>
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
        <!--    <div class="tip">-->
        <!--            必看：考勤录入，录入完缺勤人数后，请确定最后一定要点击提交按钮，如当月未有人员缺勤，请直接点击提交。-->
        <!--    </div>-->
        <!-- <el-header style="text-align: center; font-size: 30px; height:100px; line-height:95px">
          <span>电商打分系统</span>
        </el-header> -->

        <el-main>
          <div class="tip">
            必看：<br/>
            1.考勤录入时，每录入一个人员信息时，请点击录入按钮。<br/>
            2.录完人数后，请一定要点击提交按钮，如未有人员缺勤，请直接点击提交。<br/>
            3.请务必在&nbsp;20&nbsp;日之前完成提交，过时则无法完成操作！
          </div>
          <div class="main-table">
            <el-form :model="numberValidateForm" ref="numberValidateForm" label-width="100px" class="demo-ruleForm">

              <el-form-item label="员工编号" prop="ID" :rules="[{ required: true, message: '员工编号不能为空'}]">
                <el-input type="ID" v-model="numberValidateForm.ID" autocomplete="off" class="input1"
                          placeholder="请输入员工编号"></el-input>
              </el-form-item>

              <el-form-item label="姓名" prop="name" :rules="[{ required: true, message: '姓名不能为空', trigger: 'blur'}]">
                <el-input type="name" v-model="numberValidateForm.name" autocomplete="off" class="input2"
                          placeholder="请输入姓名"></el-input>
              </el-form-item>

              <el-form-item label="考核月份" prop="time" :rules="[{ required: true, message: '考核月份不能为空',trigger: 'blur'}]">
                <el-input type="age" v-model="numberValidateForm.time" autocomplete="off" class="input3"
                          placeholder="直接输入数字即可"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('numberValidateForm')">录入</el-button>
                <el-button @click="resetForm">提交</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
  import Header from "./some_components/Header.vue"
  export default {
    components:{
      Header,
    },
    data() {
      return {
        numberValidateForm: {
          name: '',
          ID: '',
          time: ''
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$confirm('此操作将录入缺勤人名单, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          customClass: 'confirmbox2',
          type: 'warning'
        }).then(() => {
          this.$axios.post('api/attence/', {
            formdata: this.numberValidateForm
          }).then(res => {
            if (res.data.num === "1") {
              this.$message({
                type: 'success',
                message: '录入成功!'
              });
            }
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消录入'
          });
        });
      },

      resetForm(formName) {
        this.$confirm('此操作将提交缺勤人名单, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          customClass: 'confirmbox2',
          type: 'warning'
        }).then(() => {
          this.$axios.post('api/table/', {}).then(res => {
            if (res.data.num === "1") {
              this.$message({
                type: 'success',
                message: '提交成功!'
              });
            }
          })
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
        let date = new Date(timeStamp).getDate() < 10 ? "0" + new Date(timeStamp).getDate() : new Date(timeStamp).getDate();
        let hh = new Date(timeStamp).getHours() < 10 ? "0" + new Date(timeStamp).getHours() : new Date(timeStamp).getHours();
        let mm = new Date(timeStamp).getMinutes() < 10 ? "0" + new Date(timeStamp).getMinutes() : new Date(timeStamp).getMinutes();
        // let ss =new Date(timeStamp).getSeconds() < 10? "0" + new Date(timeStamp).getSeconds(): new Date(timeStamp).getSeconds();
        // return year + "年" + month + "月" + date +"日"+" "+hh+":"+mm ;
        // this.nowTime = year + "年" + month + "月" + date + "日" + " " + hh + ":" + mm;
        // console.log(this.nowTime);
        // this.DATE = date;
        if (date > 31) {
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
      this.$axios.get('api/status/')
        .then(response => {
          if (response.data.first_name === "22") {
            this.loading = false
            // this.$router.push({name:"login3"})
          } else {
            this.$router.push({name: "login3"})
          }
        })
    },
    mounted() {
      this.nowTimes();
      // if (this.date>12){
      //    this.$alert('人员录入时间已超过，请联系人力资源负责人', '提示', {
      //       confirmButtonText: '确定',
      //       callback: action => {
      //         this.$router.push({name: "login3"})
      //       }
      //     });
      // }else{
      //   console.log(111)
      // }
    },
  }
</script>
<style scoped>

  .el-header {
    background-color: rgb(66, 75, 87);
    color: white;
    text-align: center;
    font-size: 30px;
    height:100px;
    line-height:95px
  }

  .tip {
    color: red;
    font-size: 25px;
    margin: 10px 50px 10px 150px;
    line-height: 40px;
    padding-top: 20px
  }

  .el-aside {
    color: #333;
    width: 300px
  }

  /*.el-main{*/
  /*  padding-top: 300px*/
  /*}*/
  .main-table {
    margin-left: 350px;
    margin-top: 100px
  }
  .tip {
    color: red;
    font-size: 15px;
    margin: 5px 0px 10px 5px;
    line-height: 20px;
  }
  .input1{
    width: 300px
  }
  .input2{
    width: 300px
  }
.input3{
    width: 300px
  }
  .menu1 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    background-color: rgb(66, 75, 87);
    color: aliceblue;
    margin-top: 10px;
    border: 1px solid #eee
  }

  .menu2 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }

  .menu3 {
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }

  /*.menu4{*/
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
  .el-main {
    font-size: 12px;
    margin-left: 0px;
    padding: 0px;
    width: 100%
  }
  .input1{
    width: 200px
  }
  .input2{
    width: 200px
  }
  .input3{
    width: 200px
  }
  .main-table {
    margin-left: 10px;
    margin-top: 20px;
    width: 100%;
  }
  }
</style>
<style>
.el-message-box, .confirmbox2{
    width: 350px
  }
</style>


