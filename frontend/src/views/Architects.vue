<script setup>

import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useInfiniteScroll } from '@vueuse/core'

const listArchitects = ref([])
const listEl = ref(null)
const fetchingData = ref(null)
const truncateText = (text) => {
  return text.length > 50 ? text.substring(0, 100) + '...' : text
}



onMounted(async (limit=6) => {
  try {
    fetchingData.value = true
    await new Promise((res) => setTimeout(res, 2000))
    const result = await axios.get(`http://localhost:3000/api/architects/?limit=${limit}&skip=${listArchitects.value.length}`)
      fetchingData.value = null
    listArchitects.value = result.data

    useInfiniteScroll(
      listEl,
      async () => {
        listArchitects.value
      },
      { distance: 10 }
    )
  } catch (error) {
    console.error('Error fetching data: ', error)
  }
})
</script>

<template>
  <div class="container mx-auto px-5">
    <section class="py-16">
      <div class="w-4/5 md:w-3/5 mx-auto">
        <h2 class="text-3xl md:text-4xl font-semibold font-theme-heading text-center">Architects</h2>
      </div>

      <ul ref="listEl" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
        <li v-for="architect in listArchitects" :key="architect.id">
          <div class="bg-white border border-gray-200 rounded-lg shadow">
            <RouterLink :to="`architects/${architect.id}`">
              <div class="aspect-w-16 aspect-h-9 h-96">
                <img
                  class="rounded-t-lg object-fill h-full w-full hover:opacity-75 transition ease-in-out duration-150"
                  :src="architect.image" alt="Architect name" />
              </div>
            </RouterLink>
            <div class="p-5">
              <RouterLink :to="`architects/${architect.id}`">
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">{{ architect.name }}</h5>
              </RouterLink>
              <p class="mb-3 font-normal text-gray-700" v-if="architect.bio.biography">{{ truncateText(architect.bio.biography) }}</p>
              <div class="flex justify-center mt-5 mb-3">
                <RouterLink :to="`architects/${architect.id}`">
                <button btn-type="primary" class="font-theme-heading text-4xl font-medium bg-gold-accent px-8 py-2 text-white rounded shadow-md hover:bg-white border-2 border-transparent hover:border-gold-accent hover:text-steel-blue cursor-pointer transition duration-200 mr-5 text-sm">Learn More</button>
                </RouterLink>
              </div>
            </div>
          </div>
        </li>
      </ul>
      <div v-show="fetchingData">
        <!-- Display a loading spinner or message -->
        <div class="text-center">
          <div role="status">
            <svg aria-hidden="true" class="inline w-10 h-10 text-gray-200 animate-spin  fill-highlight"
                 viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor" />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill" />
            </svg>
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>


    </section>
  </div>
</template>

