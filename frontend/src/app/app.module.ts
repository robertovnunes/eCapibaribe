import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserLoginComponent } from './components/user-login/user-login.component';
import { ItemCategoryComponent } from './components/item-category/item-category.component';
import { UserDataComponent } from './components/user-data/user-data.component';

@NgModule({
  declarations: [
    AppComponent,
    UserLoginComponent,
    ItemCategoryComponent,
    UserDataComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
