import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {LocalStorageService} from "../../../../service/local-storage.service";

@Component({
  selector: 'app-categories-manager',
  templateUrl: './categories-manager.component.html',
  styleUrls: ['./categories-manager.component.css']
})
export class CategoriesManagerComponent {

  constructor(private router: Router,
              private localStorage: LocalStorageService
    ) {
    if (this.localStorage.get('user') === null) {
      alert('You are not logged in!')
      this.router.navigate(['login'], {replaceUrl: true}).then(r => r);
    }
}
  onAddButtonClick() {
    this.router.navigate(['create-categories'], {replaceUrl: true}).then(r =>  r);
  }

  onListButtonClick() {
    this.router.navigate(['list-categories'], {replaceUrl: true}).then(r => r);
  }
}
