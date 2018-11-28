<template>
    <div>
        <span v-once>{{ getReserveList() }}</span>
        {{ response }}
    </div>
</template>
<script>
    import axios from "axios";
    export default{
        data:function(){
            return{
                test:'hoge',
                response: []
            }
        },
        methods: {
            getReserveList: function () {
                const request = axios.create({
                    baseURL: "http://localhost:8000/api",
                });

                request.get("/reserve/").then((response) => {
                    console.log("success");
                    this.response.push(response.data);
                }).catch(function(error) {
                    console.log(error);
                    //TODO: エラーメッセージ出す
                });
            },
        }
    }
</script>
<style>

</style>