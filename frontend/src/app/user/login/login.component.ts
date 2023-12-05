import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/services/login/login.service';
import { UserToken } from 'src/app/services/login/token';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(
    private loginService: LoginService,
    private router: Router
  ) {}
  
  login(username: string, password: string) {
    this.loginService.login<UserToken>(username, password).subscribe(
      (t) => {
        this.loginService.user_token = t.token;
        console.log(this.loginService.user_token)
      }
    )

    if (this.loginService) {
      this.router.navigate(['dashboard/'])
    }
  }


}
