<script setup>
  import PostList from './components/PostList.vue';
</script>

<template>
  <header>
    <h1>MyBlog</h1>
  </header>

  <main>
    <PostList />
  </main>
</template>

<style scoped>
header {
  text-align: center;
  padding: 20px;
  border-bottom: 1px solid #eee;
}
</style>
