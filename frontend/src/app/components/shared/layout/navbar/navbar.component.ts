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

  liLogout = document.querySelector('.logout') as HTMLLIElement;

  constructor(private readonly router: Router,
              private localStorageService: LocalStorageService) {

  }

  ngOnInit() {
    this.router.events.subscribe((val) => {
      if (val instanceof RouterEvent) {
        if (val.url === '/login' || this.localStorageService.get('user') === null) {
          this.liLogout.style.display = 'none';
        } else {
          this.liLogout.style.display = 'block';
        }
      }
    });
  }
  showComponent = false;
  NgOnChanges() {
    this.showComponent = this.router.url.includes('login')

  }
  logout() {
    this.localStorageService.set('user', null);
    this.router.navigate(['/login']).then( );
  }
}




