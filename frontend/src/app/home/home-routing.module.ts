import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from './pages/home/home.component';
import {ItemsComponent} from './pages/itens/itens.component';
import {UserLoginComponent} from "./components/user-login/user-login.component";
import {ItemCategoriesComponent} from "./components/item-categories/item-categories.component";

const routes: Routes = [
  {
    path: '',
    component: UserLoginComponent,
  },
  {
    path: 'home',
    component: HomeComponent,
  },
  {
    path: 'itens',
    component: ItemsComponent,
  },
  {
    path: 'categories',
    component: ItemCategoriesComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HomeRoutingModule {
}
