package com.example.recommender.controllers;

import com.example.recommender.services.MainService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MainController {

    @Autowired
    private MainService mainService;

    private Logger logger = LoggerFactory.getLogger(this.getClass());

//    public abstract List<Track> search(String query);
//
//    public abstract void add(Track track);
//
//    public abstract void remove(Track track);
//
//    public abstract List<Track> getRecommendation();

    @RequestMapping("/")
    public String index(){
        return "index";
    }
}
