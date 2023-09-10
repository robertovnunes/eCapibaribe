import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CadastroComponent } from './pages/cadastro/cadastro.component';
import { FormsModule } from '@angular/forms';
import { TesteApi } from './api/teste-api/teste-api.component';


@NgModule({
  providers: [
    TesteApi
  ],
  declarations: [
    CadastroComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ]
})
export class TesteModule { }
