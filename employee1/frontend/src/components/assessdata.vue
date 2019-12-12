<template>
  <div>
    <Header></Header>
    <el-container style="height:1000px">
      <el-aside class="aside">
        <div class="menu1"></div>
        <div class="menu2"></div>
        <div class="menu3">部门考核详情</div>
        <!--        <div class="menu4">小ceo月绩效打分</div>-->
        <div class="menu5"></div>
        <div class="menu6"></div>
      </el-aside>

  <el-container>


    <el-main>
<div class="main-table">

        <div class="toexcel">
            <el-button  @click="exportExcel" type="primary" class="button" style="width:70px;top:0;right:30px">导出</el-button>
        </div>
        <!-- <el-table class="table" :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%"> -->
        <el-table class="table" ref="filterTable" :data="tableData" style="width: 100%">
            <el-table-column prop="bumen" label="部门" min-width="80%" align="center" ></el-table-column>
            <el-table-column
              prop="time"
              label="考核月份"
              align="center"
              min-width="50%"
              column-key="month"
              :filters="[{text: '1', value: '1'},{text: '2', value: '2'},{text: '3', value: '3'},{text: '4', value: '4'},{text: '5', value: '5'},{text: '6', value: '6'},{text: '7', value: '7'},{text: '8', value: '8'},{text: '9', value: '9'},{text: '10', value: '10'},{text: '11', value: '11'},{text: '12', value: '12'}]"
              :filter-method="filterHandler"
            >
            </el-table-column>
          <el-table-column prop="dafen" label="考核分数" align="center" min-width="90%"></el-table-column>
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
import Header from "./some_components/Header"
export default {
  components:{
    Header,
  },
  data() {
    return {
        tableData: [
          {
          bumen: "",
          time: "",
          dafen: ""
        }
        ]

        //  currentPage: 1, // 当前页码
        //     total: 20, // 总条数
        //     pageSize: 10 // 每页的数据条数
    };
  },
  methods: {
    filterHandler(value, row, column) {
        console.log('value:'+value)
        console.log('row:'+row)
        console.log('column:'+column)
        const property = column['property'];
        console.log('row[property]:'+row[property]);
        return row[property] === value;
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
          if (response.data.first_name === "11" ) {
            this.loading = false
            // this.$router.push({name:"login3"})
            this.$axios.get('api/assessdata/')
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
.toexcel {
  cursor: pointer;
  cursor: hand;
  width: 70px;
  height: 34px;
}
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
    background-color:  rgb(66, 75, 87);
    color: aliceblue;
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
