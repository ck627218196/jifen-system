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


    <el-main>
<div class="main-table">

        <div class="toexcel">
          <el-row>
            <el-button  @click="exportExcel" type="primary" class="button" style="width:70px;top:0;right:30px">导出</el-button>
            <el-button  @click="permission" type="primary" class="button" >权限管理</el-button>
          </el-row>
        </div>
        <!-- <el-table class="table" :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%"> -->
        <el-table class="table" ref="filterTable" :data="tableData" style="width: 100%">
            <el-table-column prop="jobnum" label="工号" min-width="45%"></el-table-column>
            <el-table-column prop="name" label="姓名" min-width="60%"></el-table-column>
            <el-table-column prop="department" label="部门" min-width="80%"></el-table-column>
            <el-table-column
              prop="month"
              label="考核月份"
              min-width="50%"
              column-key="month"
              :filters="[{text: '1', value: '1'},{text: '2', value: '2'},{text: '3', value: '3'},{text: '4', value: '4'},{text: '5', value: '5'},{text: '6', value: '6'},{text: '7', value: '7'},{text: '8', value: '8'},{text: '9', value: '9'},{text: '10', value: '10'},{text: '11', value: '11'},{text: '12', value: '12'}]"
              :filter-method="filterHandler"
            >
            </el-table-column>
<!--            <el-table-column prop="marks" label="考核分数" min-width="40%"></el-table-column>-->
            <el-table-column prop="level" label="考核等级" min-width="40%"></el-table-column>
            <el-table-column prop="jifen" label="员工积分" min-width="45%"></el-table-column>
        </el-table>
        <!-- 分页器 -->
       <!-- <div class="block" style="margin-top:15px;">
            <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[1,5,10,20]" :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="tableData.length">
            </el-pagination>
        </div> -->
        <!-- 分页器 -->
</div>
    </el-main>
  </el-container>
</el-container>
  </div>
  </template>


<script>
import FileSaver from "file-saver";
import XLSX from "xlsx";
import Header from "./some_components/Header";
export default {
  components:{
    Header,
  },
  data() {
    return {
        lastdate:'31',
        tableData: [
          {
          jobnum: "0896925",
          name: "陈吉康",
          department: "互联网系统运营中心",
          month: "7",
          // marks: "95",
          level: "A",
          jifen: "100"
        }
        ]

        //  currentPage: 1, // 当前页码
        //     total: 20, // 总条数
        //     pageSize: 10 // 每页的数据条数
    };
  },
  methods: {
    // 表格筛选功能
    filterHandler(value, row, column) {
        console.log('value:'+value)
        console.log('row:'+row)
        console.log('column:'+column)
        const property = column['property'];
        console.log('row[property]:'+row[property]);
        return row[property] === value;
      },

    permission(){
      this.$router.push({name:"permission"});
    },

    // 开放其他账号的权限
    useropen(){
      this.$confirm('此操作将开放各位经理的登录权限, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
            this.$axios.post('api/useropen/',{
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
        });
    },

    // 分页所用
    // handleSizeChange(val) {
    //         console.log(`每页 ${val} 条`);
    //         this.currentPage = 1;
    //         this.pageSize = val;
    //     },
    //     handleCurrentChange(val) {
    //         console.log(`当前页: ${val}`);
    //         this.currentPage = val;
    //     },

    //导出表格所用


    // cellstyle(){
    //     return 'text-align: center'
    // },
    // 设置el-table样式


    exportExcel() {
      // 设置当前日期
      let time = new Date();
      let year = time.getFullYear();
      let month = time.getMonth() + 1;
      let day = time.getDate();
      let name = year + "" + month + "" + day;
      // console.log(name)
      /* generate workbook object from table */
      //  .table要导出的是哪一个表格
      var wb = XLSX.utils.table_to_book(document.querySelector(".table"));
      /* get binary string as output */
      var wbout = XLSX.write(wb, {
        bookType: "xlsx",
        bookSST: true,
        type: "array"
      });
      try {
        //  name+'.xlsx'表示导出的excel表格名字
        FileSaver.saveAs(
          new Blob([wbout], { type: "application/octet-stream" }),
          name + ".xlsx"
        );
      } catch (e) {
        if (typeof console !== "undefined") console.log(e, wbout);
      }
      return wbout;
    }
  },
  created () {
      this.$axios.get('api/status/')
        .then(response => {
          if (response.data.first_name === "66" ) {
            this.loading = false
            // this.$router.push({name:"login3"})
            this.$axios.get('api/download/')
              .then(response => {
                this.tableData = response.data.data
                })
          } else {
            this.$router.push({name:"login3"})
          }
        })
    }
};
</script>
<style scoped>
/* 导出按钮 */
/*.toexcel {*/
/*  cursor: pointer;*/
/*  cursor: hand;*/
/*  !*width: 70px;*!*/
/*  !*height: 34px;*!*/
/*}*/
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
  .main-table{
      margin-left: 120px;
      width: 82%;
  }
  .el-table{
    font-size: 20px
  }
  .menu1{
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    margin-top: 10px;
    border: 1px solid #eee
  }
  .menu2{
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }
  .menu3{
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
  .menu5{
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee
  }
  .menu6{
    height: 100px;
    width: 290px;
    font-size: 22px;
    text-align: center;
    line-height: 100px;
    border: 1px solid #eee;
    background-color:  rgb(66, 75, 87);
    color: aliceblue;
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
  .el-main {
    font-size: 12px;
    margin-left: 0px;
    padding: 0px;
  }
  .el-table {
    font-size: 12px;
    width: 100%;
  }
  }
</style>
