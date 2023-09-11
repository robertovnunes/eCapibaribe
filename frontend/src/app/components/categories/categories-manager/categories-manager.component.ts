import { Component } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-categories-manager',
  templateUrl: './categories-manager.component.html',
  styleUrls: ['./categories-manager.component.css']
})
export class CategoriesManagerComponent {


  constructor(private router: Router) { }
  onAddButtonClick() {
    this.router.navigate(['create-categories'], {replaceUrl: true}).then(r =>  r);
  }

  onListButtonClick() {
    this.router.navigate(['list-categories'], {replaceUrl: true}).then(r => r);
  }
}
