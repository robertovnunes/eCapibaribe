import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegistrarComponent } from './pages/registrar/registrar.component';
import { ItemsApi } from './api/items-api';
import { FormsModule } from '@angular/forms';
import { InventarioComponent } from './pages/inventario/inventario.component';
import {MatTableModule} from '@angular/material/table';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';


@NgModule({
  declarations: [
    RegistrarComponent,
    InventarioComponent
  ],
  providers: [
    ItemsApi
  ],
  imports: [
    CommonModule,
    FormsModule,
    MatTableModule,
    MatIconModule,
    MatButtonModule
  ]
})
export class ItemsModule { }
