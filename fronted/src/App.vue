<script setup>
  import PostList from './components/PostList.vue';
</script>

<template>
  <el-container class="OuterCon">
    <el-header class="bg-gray-100 text-center p-4 border-b border-gray-200">
      <h3>MyBlog</h3>
    </el-header>

    <el-main><PostList /></el-main>

    <el-footer  class="text-center text-gray-500 p-4 border-t border-gray-200">
      <h5>@2025 我的博客</h5>
    </el-footer>
  </el-container>
</template>

<style scoped>
</style>
