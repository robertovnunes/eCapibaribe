import { Component, OnInit } from '@angular/core';
import { ItemsApi } from '../../api/items-api';
import { Router } from '@angular/router';
import { Item, defaultItem } from '../../types/items';
import { Observable, ReplaySubject } from 'rxjs';
import { ItemsState } from '../../state/items.state';

@Component({
  selector: 'app-editar',
  templateUrl: './editar.component.html',
  styleUrls: ['./editar.component.css']
})
export class EditarComponent implements OnInit {
  item: Item = defaultItem;

  constructor(private itemsApi: ItemsApi, private _router: Router, private state: ItemsState) { }
  
  ngOnInit(): void {
    console.log("ngOnInit");
    this.state.getCurrentItemId().subscribe((id: number) => {
      this.itemsApi.getSingleItem(id=id).subscribe((response: any) => {
        this.item = response;
      })
    });
  }
  
  onSubmit() {
    this.itemsApi.alterarItem(this.item).subscribe((response: any)=> {
      console.log(response);
      this._router.navigateByUrl('/items/inventario');
    })
  }

  convertFile(file : File) : Observable<string> {
    const result = new ReplaySubject<string>(1);
    const reader = new FileReader();
    reader.readAsBinaryString(file);
    reader.onload = (event: any) => result.next(btoa(event.target.result.toString()));
    return result;
  }

  receiveImage(event: any){
    const file:File = event.target.files[0];
      
    if (file) {
      this.convertFile(event.target.files[0]).subscribe(base64 => {
        this.item.imagem = `data:image/png;base64,${base64}`;
      });
    }
  }


}
