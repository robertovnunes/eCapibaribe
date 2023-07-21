import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserLoginComponent} from "./home/components/user-login/user-login.component";
import {HomeComponent} from "./home/pages/home/home.component";

const routes: Routes = [
    {path: '', component: UserLoginComponent},
    {path: 'home', component: HomeComponent}
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
