<template>
    <div class="post-list">
        <h2>文章列表</h2>

        <div v-if="isLoading" class="loading">正在加载文章/Posts are loading...</div>
        <div v-else-if="error" class="error">{{ error }}</div>

        <div v-else>
            <div v-for="post in psots" :key="post.id" class="post-item">
                <h4>{{ post.title }}</h4>
                
                <p class="post-meta">
                    <span>分类：{{ post.category?.name || '未分类' }}</span>
                    <span>发布于: {{ new Date(post.created_at).toLocaleDateString() }}</span>
                </p>

                <div class="post-content">
                    <p>{{ post.context }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import {ref,onMounted} from 'vue';
    import axios from 'axios';

    // 创建响应式变量存储文章列表
    const psots = ref([]);
    const isLoading = ref(true); // 用于显示加载状态
    const error = ref(null); // 用于存放错误信息

    // 获取数据::异步函数
    const fetchPosts = async() => {
        try{
            const response = await axios.get('http://127.0.0.1:8000/api/posts');

            psots.value = response.data;
            console.log('成功获取文章数据：',response.data);
        }catch(err){
            console.error('获取文章数据失败：',err);
            err.value = "无法获取文章列表，请稍后再试。";
        }finally{
            isLoading.value = false;
        }
    }

    onMounted(() => {
        fetchPosts();
    })
</script>

<style scoped>
.post-list {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
}
.post-item {
  border-bottom: 1px solid #eee;
  padding: 20px 0;
}
.post-item:last-child {
  border-bottom: none;
}
.post-item h3 {
  margin: 0 0 10px;
}
.post-meta {
  color: #888;
  font-size: 0.9em;
}
.post-meta span {
  margin-right: 15px;
}
.loading, .error {
  text-align: center;
  padding: 40px;
  color: #888;
}
</style>