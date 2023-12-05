import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { LoginService } from 'src/app/services/login/login.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit{
  constructor(
    private loginService: LoginService,
    private router: Router,
    private activateRoute: ActivatedRoute
  ) {}

  hideLogin: boolean = true;
  ngOnInit(): void {
    if (this.loginService.user_token) {
      console.log(this.loginService.user_token);
      this.hideLogin = false;
    }
  }

  logout() {
    if (!this.loginService.user_token) {
      alert("No user found");
    } else {
      this.loginService.user_token = undefined;
    
      if (this.loginService) {
        console.log(this.loginService.user_token);
        this.router.navigate(['login/'])
      } 
    }
    
  }
}
