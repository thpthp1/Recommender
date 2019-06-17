package com.example.recommender.models;

import javax.persistence.*;
import java.sql.Time;
@Entity
public class Track {

    @Column(name = "track_id")
    @Id
    private String id;

    @Column(name = "track_name")
    private String name;

    @Column(name = "art_link")
    private String artLink;

    @Column(name = "BPM")
    private int bpm;

    @Column(name = "track_length")
    private Time length;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getArtLink() {
        return artLink;
    }

    public void setArtLink(String artLink) {
        this.artLink = artLink;
    }

    public int getBpm() {
        return bpm;
    }

    public void setBpm(int bpm) {
        this.bpm = bpm;
    }

    public Time getLength() {
        return length;
    }

    public void setLength(Time length) {
        this.length = length;
    }
}