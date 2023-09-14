import {Component, OnInit,Inject} from '@angular/core';
import { Item, showItem } from '../../types/items';
import { ItemsApi } from '../../api/items-api';
import { ItemsState } from '../../state/items.state';
import { Router } from '@angular/router';
import {MatDialog, MAT_DIALOG_DATA, MatDialogRef, MatDialogModule} from '@angular/material/dialog';
import {MatButtonModule} from '@angular/material/button';
import {FormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';

@Component({
  selector: 'app-inventario',
  templateUrl: './inventario.component.html',
  styleUrls: ['./inventario.component.css']
})
export class InventarioComponent implements OnInit {
  displayedItems: string[] = ['Item-ID', 'Nome', 'Preço', 'Marca', 'Quantidade', 'Categoria', 'Imagem', 'Editar'];
  itemSource: showItem[] = [];

  constructor(private itemsApi: ItemsApi, private state: ItemsState, private _router: Router,
    public dialog: MatDialog
  ) {}

  ngOnInit(): void {
    this.itemsApi.getitems().subscribe((response: any)=> {
      response = response as Item[];
      let newItems: showItem[] = [];
      response.forEach((element: Item) => {
        newItems.push({
          item_id: element.item_id, 
          item_nome: element.item_nome, 
          item_price: element.item_price, 
          marca: element.marca, 
          quantidade: element.quantidade, 
          categoria: element.categoria, 
          imagem: element.imagem
        });
      });
      this.itemSource = newItems;
    });
  }

  onEdit(id:number) {
    this.state.setCurrentItemId(id);
    console.log(id);
    this._router.navigateByUrl('/items/editar');

  }

  onDelete(id:number) {
    const dialogRef = this.dialog.open(DialogOverviewExampleDialog, {
      data: id
    });
    
    dialogRef.afterClosed().subscribe(result => {
      if(result === true) {
        this.itemsApi.removerItem(id).subscribe((response:any) => {
          try {
            let index = this.itemSource.findIndex((item:any) => {
              return id === item.item_id;
            })
            let arrayShowItem: showItem[] = [];
            for (let i = 0;i<this.itemSource.length; i++){
              if(i === index) continue;
              arrayShowItem.push(this.itemSource[i]);
            }
            this.itemSource = arrayShowItem;
            alert(`Item ${response.msg} deletado com sucesso!`);
          } catch { 
            alert("Não encontrado");
          }
        });
      }
    });
  }

}

@Component({
  selector: 'delete-dialog',
  templateUrl: 'delete-dialog.html',
  standalone: true,
  imports: [MatDialogModule, MatFormFieldModule, MatInputModule, FormsModule, MatButtonModule]
})
export class DialogOverviewExampleDialog {
  constructor(
    public dialogRef: MatDialogRef<DialogOverviewExampleDialog>,
    @Inject(MAT_DIALOG_DATA) public data: number,
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
}