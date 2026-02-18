import Index from '@/components/Index'
import Login from '@/components/Auth/Login'
import Logout from '@/components/Auth/Logout'
import ResetPassword from '@/components/Auth/ResetPassword'

import Promo from '@/components/Promocodes/Promocodes'
import CPromo from '@/components/Promocodes/createPromo'
import FDStats from '@/components/Promocodes/findDayStats'
import FMStats from '@/components/Promocodes/findMonthStats'
import FTMStats from '@/components/Promocodes/findTMonthStats'

import Edit from '@/components/Edit/Edit'
import Dashboard from '@/components/Dashboard/Dashboard'
import API from '@/components/API/API'
import Error404 from '@/components/404/Error404'

const routes = [
  {
    path: '/',
    name: 'Main page',
    component: Index
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/log-out',
    name: 'Log-out',
    component: Logout
  },
  {
    path: '/reset-password',
    name: 'Reset-Password',
    component: ResetPassword
  },
  {
    path: '/promo',
    name: 'Promo List',
    component: Promo
  },
  {
    path: '/promo/create',
    name: 'Create Promo',
    component: CPromo
  },
  {
    path: '/promo/fd-stats',
    name: 'Find day stats',
    component: FDStats
  },
  {
    path: '/promo/fm-stats',
    name: 'Find month stats',
    component: FMStats
  },
  {
    path: '/promo/ftm-stats',
    name: 'Find total month stats',
    component: FTMStats
  },
  {
    path: '/edit',
    name: 'Edit',
    component: Edit
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/api',
    name: 'API',
    component: API
  },
  {
    path: '*',
    name: 'Error 404',
    component: Error404
  }
]

export { routes }



// WEBPACK FOOTER //
// src/router/index.js