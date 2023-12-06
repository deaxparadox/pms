import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, provideHttpClient } from '@angular/common/http';
import { BrowserAnimationsModule} from "@angular/platform-browser/animations"

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeadingComponent } from './components/heading/heading.component';
import { NavbarComponent } from './layout/navbar/navbar.component';
import { FooterComponent } from './layout/footer/footer.component';
import { LeftComponent } from './layout/row/left/left.component';
import { RightComponent } from './layout/row/right/right.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TaskComponent } from './components/task/task.component';
import { HeadingDetailComponent } from './components/heading-detail/heading-detail.component';
import { TaskDetailComponent } from './components/task-detail/task-detail.component';
import { LoginComponent } from './user/login/login.component';
import { SignupComponent } from './user/signup/signup.component';
import { ChatComponent } from './chat/chat.component';

@NgModule({
  declarations: [
    AppComponent,
    HeadingComponent,
    NavbarComponent,
    FooterComponent,
    LeftComponent,
    RightComponent,
    DashboardComponent,
    TaskComponent,
    HeadingDetailComponent,
    TaskDetailComponent,
    LoginComponent,
    SignupComponent,
    ChatComponent,
    // HeroesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
