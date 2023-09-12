import { NgModule } from '@angular/core';
import { Routes, RouterModule } from "@angular/router";
import { LoginComponent } from "./components/pages/login/login.component";
import { HomeComponent } from "./components/home/home.component";
import { CreateCategoriesComponent } from "./components/pages/categories/create-categories/create-categories.component";
import { CategoriesManagerComponent } from "./components/pages/categories/categories-manager/categories-manager.component";
import { ListCategoriesComponent } from "./components/pages/categories/list-categories/list-categories.component";

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'categories', component: CategoriesManagerComponent},
  { path: 'create-categories', component: CreateCategoriesComponent },
  {path: 'list-categories', component: ListCategoriesComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})

export class AppRoutingModule { }
