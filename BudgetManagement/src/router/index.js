import { createRouter, createWebHistory } from 'vue-router'
import Menu from '@/views/Menu.vue'
import Profil from '@/views/Profil.vue'
import AddExpense from '@/views/AddExpense.vue'
import UserCategory from '@/views/UserCategory.vue'
import UserExpenses from '@/views/UserExpenses.vue'
import CreateAccount from '@/views/CreateAccount.vue'
import UserStats from '@/views/UserStats.vue'
import ConnectAccount from '@/views/ConnectAccount.vue'


const routes = [
    {path : '/menu', name: 'Menu', component: Menu},
    {path : '/profil', name: 'Profil', component: Profil},
    {path : '/add-expense', name: 'addExpense', component: AddExpense},
    {path : '/categories', name: 'UserCategory', component: UserCategory},
    {path : '/expenses', name: 'UserExpenses', component: UserExpenses},
    {path : '/create', name: 'CreateAccount', component: CreateAccount},
    {path : '/stats', name: 'UserStats', component: UserStats},
    {path : '/connect', name: 'ConnectAccount', component: ConnectAccount}
]

const router = createRouter(
    {
        history : createWebHistory(),
        routes
    })

export default router