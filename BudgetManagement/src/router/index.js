import { createRouter, createWebHistory } from 'vue-router'
import Menu from '@/views/Menu.vue'
import Categories from '@/views/Categories.vue'



const routes = [
    {path : '/menu', name: 'Menu', component: Menu},
    {path : '/categories', name: 'Categories', component: Categories}
]

const router = createRouter(
    {
        history : createWebHistory(),
        routes
    })

export default router