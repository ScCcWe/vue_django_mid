<template>
  <div>
    <div class="goods_list" v-for="(item, index) in goods_list" :key="index">
      <ul>
        <li>{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Goods",
  data() {
    return {
      goods_list: []
    };
  },
  created() {
    axios.get("http://127.0.0.1:8000/goods/").then(res => {
      this.goods_list = res.data.results;
    });
  }
};
</script>

<style scoped></style>
