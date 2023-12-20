<script setup>

import Header from './sections/Header.vue'
import Main from './views/Home.vue'
import Footer from './sections/Footer.vue'

</script>

<template>
  <Header />
  <Suspense>
    <RouterView />
    <template #fallback>
      <p>Loading...</p>
    </template>
  </Suspense>

  <Footer />
</template>

<style scoped></style>
