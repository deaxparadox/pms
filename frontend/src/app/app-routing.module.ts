import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeadingComponent } from './components/heading/heading.component';
import { HeadingDetailComponent } from './components/heading-detail/heading-detail.component';

const routes: Routes = [
  {path: "dashboard", component: DashboardComponent},
  {path: "heading", component: HeadingComponent},
  {path: "heading/:id", component: HeadingDetailComponent},
  { path: '', redirectTo: "/dashboard", pathMatch: "full"}
  // { path: '', redirectTo: "/dashboard", pathMatch: "full"}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
