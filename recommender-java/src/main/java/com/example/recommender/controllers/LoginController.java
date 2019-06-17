package com.example.recommender.controllers;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.io.IOException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Objects;

@Controller
public class LoginController {

    @Autowired
    private Environment environment;

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    @Value("${app.oauth2.client_id}")
    private String clientId;

    @Value("${app.oauth2.client_secret}")
    private String clientSecret;

    @Value("${app.oauth2.scopes}")
    private String scopes;

    @Value("${app.oauth2.callback_uri}")
    private String callbackURI;

    @Value("${app.oauth2.auth_address}")
    private String authorizeEndpoint;

    @GetMapping("/login")
    public String login(){
        String authURI = "";
        try {
            authURI = authorizeEndpoint + "?response_type=code"
                    + "&client_id=" + clientId
                    + "&client_secret=" + clientSecret
                    + "&scope=" + URLEncoder.encode(scopes, StandardCharsets.UTF_8.toString())
                    + "&redirect_uri=" + URLEncoder.encode(callbackURI, StandardCharsets.UTF_8.toString());
            logger.info(authURI);
        }
        catch(IOException e){
            e.printStackTrace();
        }
        return "redirect:" + authURI;
    }

    @RequestMapping("/callback")
    public String callback(@RequestParam(value = "code", required = false) String code,
                        @RequestParam(value = "state", required = false) String state){
        Objects.requireNonNull(code, "Wrong callback URI");
        logger.info(code);
        logger.info(state);
        return "redirect:/";
    }
}
