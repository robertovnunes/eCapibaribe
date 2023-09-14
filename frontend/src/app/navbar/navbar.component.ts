import { Component, OnInit } from '@angular/core';
import { Router, RouterEvent } from "@angular/router";
import { LocalStorageService } from '../service/local-storage.service';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  liLogout: HTMLLIElement | null = document.querySelector('.liLogout');
  isLogedIn: boolean = false;

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
    if (confirm('Are you sure you want to logout?')) {
      this.localStorageService.remove('user');
      this.router.navigate(['/login']).then();
    }
  }
}
