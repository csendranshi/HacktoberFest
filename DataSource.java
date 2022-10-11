package com.beans;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
public class DataSource {
	
	List<Product> list = new ArrayList<>(); //ctrl + shift + O
	public void populate(){
		Product p1 = new Product();
		p1.setId(1);
		p1.setTitle("Oppo Mobile Phone");
		p1.setPrice(13000.50);
		p1.setStockCount(12);
		p1.setCategory("Mobile");
		this.list.add(p1);
		p1 = new Product();
		p1.setId(2);
		p1.setTitle("Samsung Mobile Phone");
		p1.setPrice(18000.00);
		p1.setStockCount(9);
		p1.setCategory("Mobile");
		this.list.add(p1);
		p1 = new Product();
		p1.setId(3);
		p1.setTitle("HP Blaze 780");
		p1.setPrice(48000.00);
		p1.setStockCount(5);
		p1.setCategory("Laptop");
		this.list.add(p1);
		
		p1 = new Product();
		p1.setId(4);
		p1.setTitle("Dell Latitude 230");
		p1.setPrice(38000.00);
		p1.setStockCount(7);
		p1.setCategory("Laptop");
		this.list.add(p1);
		
		p1 = new Product();
		p1.setId(5);
		p1.setTitle("Acer Desktop PC");
		p1.setPrice(32000.00);
		p1.setStockCount(2);
		p1.setCategory("Desktop");
		this.list.add(p1);
	}
	public List<Product> getList() {
		return list;
	}
	public List<Product> processStockCountFilter(List<Product> list, int count) {
		 list = list.stream()
				 .filter(p-> p.getStockCount() >=count)
				 .collect(Collectors.toList());
		return list;
	}
	public List<Product> processPriceSort(List<Product> list) {
		 list = list.stream()
				 .sorted((p1,p2)-> p2.getPrice().compareTo(p1.getPrice()))
				 .collect(Collectors.toList());
		return list;
	}
	public List<Product> processFilterOnMobileAndLaptop(List<Product> list, List<String> catList) {
		 list = list.stream().filter(p-> catList.contains(p.getCategory()))
				 .collect(Collectors.toList());
		return list;
	}
	 
	
}
