<template>
  <div class="Category">
    <h1>分类页面</h1>
<!--    {{ category_list }}-->
    <div
      class="category_list"
      v-for="(item, index) in category_list"
      :key="index"
    >
      <ul>
        <li>{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import { getCategory } from "../api/api";

export default {
  data() {
    return {
      category_list: []
    };
  },
  created() {
    getCategory()
      .then(res => {
        this.category_list = res.data.results;
      })
      .catch(function(error) {
        console.log(error);
      });
  }
};
</script>
