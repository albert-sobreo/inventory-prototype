Vue.component('sidebar', {
    props: [
        'active',
    ],

    data: function(){
        return{
            branches: [{
                pk: null,
                name: null,
            }]
        }
    },
    
    mounted(){
        fetch('/getsidebarbranchdata/')
        .then(res=>res.json())
        .then(data=>this.branches=data);
        var element = document.getElementById(this.active)
        element.classList.add('sidenav-active')
    },
    
    created(){
    },
    
    template: `<div class="sidenav">
                    <div class="sidenav-brand">
                        <!-- Insert Logo here -->
                        <img src="/static/media/admin.svg" alt="">
                    </div>
                    <div class="sidenav-body">
                        <a href="/top-level/home/" class="sidenav-link" id='home'>Home</a>
                        <a href="#" class="sidenav-link" id='branch'>Branch</a>
                        <div id="wrapper">
                            <div id="list">
                                <a v-for='branch in branches' :href="'/top-level/branch/'+ branch.pk +'/inventory/'" class="wrapper-link">{{branch.name}}</a>
                            </div>
                        </div>
                        <a href="#" class="sidenav-link" id='employees'>Employees</a>
                        <a href="#" class="sidenav-link" id='customers'>Customers</a>
                        <a href="#" class="sidenav-link" id='suppliers'>Suppliers</a>
                        <div class="sidenav-break"></div>
                        <a href="#" class="sidenav-link" id='purchase'>Purchase</a>
                        <a href="#" class="sidenav-link" id='sales'>Sales</a>
                        <a href="#" class="sidenav-link" id='transfers'>Transfers</a>
                        <a href="#" class="sidenav-link" id='spoilage'>Spoilage</a>
                        <a href="#" class="sidenav-link" id='approvals'>Approvals</a>
                    </div>
                </div>`
});