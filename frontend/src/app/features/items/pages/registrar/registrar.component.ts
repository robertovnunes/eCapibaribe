import { Component } from '@angular/core';
import { Item, defaultItem } from '../../types/items';
import { ItemsApi } from '../../api/items-api';
import { Router } from '@angular/router';
import { Observable, ReplaySubject } from 'rxjs';


@Component({
  selector: 'app-registrar',
  templateUrl: './registrar.component.html',
  styleUrls: ['./registrar.component.css']
})

export class RegistrarComponent {
  item: Item = defaultItem;
  constructor(private itemsApi: ItemsApi, private _router: Router) { }
    
  ngOnInit(): void {
    
  }
  
  onSubmit() {
    this.itemsApi.cadastrarItem(this.item).subscribe((response: any)=> {
      console.log(response);
      if(response.msg = "Item registrado com sucesso!"){
        this._router.navigateByUrl('/items/inventario');
      }else{
        alert(response.msg);
      }
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
