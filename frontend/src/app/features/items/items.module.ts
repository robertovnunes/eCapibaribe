import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegistrarComponent } from './pages/registrar/registrar.component';
import { ItemsApi } from './api/items-api';
import { FormsModule } from '@angular/forms';
import { InventarioComponent } from './pages/inventario/inventario.component';
import {MatTableModule} from '@angular/material/table';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import { EditarComponent } from './pages/editar/editar.component';
import {MatDialogModule} from '@angular/material/dialog';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';


@NgModule({
  declarations: [
    RegistrarComponent,
    InventarioComponent,
    EditarComponent
  ],
  providers: [
    ItemsApi
  ],
  imports: [
    CommonModule,
    FormsModule,
    MatTableModule,
    MatIconModule,
    MatButtonModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
  ]
})
export class ItemsModule { }
