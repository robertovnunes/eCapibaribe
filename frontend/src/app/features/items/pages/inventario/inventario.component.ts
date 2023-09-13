import {Component, OnInit} from '@angular/core';
import { Item, showItem } from '../../types/items';
import { ItemsApi } from '../../api/items-api';

@Component({
  selector: 'app-inventario',
  templateUrl: './inventario.component.html',
  styleUrls: ['./inventario.component.css']
})
export class InventarioComponent implements OnInit {
  displayedItems: string[] = ['Item-ID', 'Nome', 'Preço', 'Marca', 'Quantidade', 'Categoria', 'Imagem'];
  itemSource: showItem[] = [];

  constructor(private itemsApi: ItemsApi) { }

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

}
