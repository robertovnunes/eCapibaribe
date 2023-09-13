import {Component, OnInit} from '@angular/core';
import {Router, RouterEvent} from "@angular/router";
import {User} from "../../../../service/interfaces/user";
import {LocalStorageService} from "../../../../service/local-storage.service";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  liLogout: HTMLLIElement|null = document.querySelector('.liLogout');
  isLogedIn:boolean = false;

  constructor(private readonly router: Router,
              private localStorageService: LocalStorageService) {

  }

  ngOnInit() {
    this.router.events.subscribe((val) => {
      if (val instanceof RouterEvent) {
        if (val.url === '/login' || this.localStorageService.get('user') === null) {
          this.isLogedIn = false;
        } else {
          this.isLogedIn = true;
        }
      }
    });
  }

  logout() {
    this.localStorageService.set('user', null);
    this.router.navigate(['/login']).then( );
  }
}




