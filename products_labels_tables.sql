create database products_lables;
use products_lables;
create table ProApp(
	label varchar(40) primary key not null,
	product varchar(40),
    typeproduct varchar(40) not null,
	ingredients text(1000000) not null);
    
select * from ProApp;
delete from ProApp;
drop table ProApp;
drop database products_lables; 

-- --------------Procedure tra bảng------------------------------------
DELIMITER $$
CREATE procedure Searchlabels(Pylabel varchar(50))
BEGIN
	select * from ProApp where label = Pylabel;
END $$
DELIMITER ;
call Searchlabels('PC_BHA');

drop procedure Searchlabels;

-- -------------------------------------------------------------------
insert into ProApp(label,product,typeproduct,ingredients)
value
('PC_BHA','Paulas Choice', 'Tẩy tế bào chết','Aqua, Methylpropanediol,Butylene Glycol, Salicylic Acid, Polysorbate 20, Camellia Oleifera (Green tea) Leaf Extract, Sodium Hydroxide, Tetrasodium EDTA'),
('PC_Retinol','Paulas Choice','Kem dưỡng','Aqua, Dimethicone, Glycerin, Butylene Glycol, Isononyl Isononanoate, Castor Isostearate Succinate, Glyceryl Stearate, C12-15 Alkyl Benzoate, Dimethicone Crosspolymer, PEG-33, Polysorbate 20, Behenyl Alcohol, Retinol, Tetrahexyldecyl Ascorbate, Ceramide 2, Palmitoyl Oligopeptide, Palmitoyl Tetrapeptide-7, Sodium Hyaluronate, Dipotassium Glycyrrhizate, Glycyrrhiza Glabra (Licorice) Root Extract, Avena Sativa (Avena) Kernel Extract, Arctium Lappa (Burdock) Root Extract, Salix Alba (Willow) Bark Extract, Glycine Soja Sterols, Lecithin, Allantoin, Tocopheryl Acetate, Hydrolyzed Soy Protein, Sorbitan Laurate, Acetyl Dipeptide-1 Cetyl Ester, Disodium EDTA, Hydroxyethylcellulose, Sodium Hydroxide, Tribehenin, Caprylyl Glycol, Ethylhexylglycerin, Pentylene Glycol, PEG-100 Stearate, PEG-75 Shea Butter Glycerides, PPG-12/​Smdi Copolymer, PEG-10 Phytosterol, PEG-8 Dimethicone, PEG-14, Pentaerythrityl Tetraisostearate, Polymethylsilsesquioxane, Magnesium Aluminum Silicate, Arachidyl Glucoside, Sclerotium Gum, Arachidyl Alcohol, Benzoic Acid, Sodium Carbomer, Phenoxyethanol'),
('Simple_TayTrang','Simple','Tẩy trang', 'Aqua, Hexylene Glycol, Glycerin, Cetrimonium Chloride, Cetylpyridinium Chloride, Chamomilla Recutita Flower Extract, Citric Acid, Niacinamide, Panthenol, Pantolactone, PEG-6 Caprylic/​Capric Glycerides, Phenoxyethanol, Potassium Chloride, Propylene Glycol, Sodium Ascorbyl Phosphate, Sodium Chloride, Tetrasodium EDTA'),
('Skin1004_KCN','Skin1004','Kem chống nắng', 'Centella Asiatica Extract (29.4%), Cyclomethicone, Zinc Oxide, Water, Titanium Dioxide (Ci 77891), Dicaprylyl Carbonate, Propanediol, Polyglyceryl-3 Polydimethylsiloxyethyl Dimethicone, Niacinamide, Caprylyl Methicone, Cetyl Ethylhexanoate, 1,2-Hexanediol, Methyl Methacrylate Crosspolymer, Betaine, Magnesium Sulfate, Disteardimonium Hectorite, Hydrogen Dimethicone, Polymethylsilsesquioxane, Inositol, Aluminum Hydroxide, C30-45 Alkyl Cetearyl Dimethicone Crosspolymer, Polyglyceryl-2 Dipolyhydroxystearate, Styrene/​Acrylates Copolymer, Stearic Acid, Butylene Glycol, Pentylene Glycol, Dextrin, Theobroma Cacao (Cocoa) Extract, Coptis Chinensis Root Extract, Helianthus Annuus (Sunflower) Seed Oil, Citrus Aurantium Bergamia (Bergamot) Fruit Oil, Ethylhexylglycerin, Octyldodecanol, Madecassoside, Pelargonium Graveolens Flower Oil, Echium Plantagineum Seed Oil, Rosa Damascena Flower Oil, Cardiospermum Halicacabum Flower/​Leaf/​Vine Extract, Helianthus Annuus (Sunflower) Seed Oil Unsaponifiables, Dibutyl Adipate, Undecane, Sodium Hyaluronate, Tridecane, Tocopherol'),
('Skin1004_KemDuong','Skin1004','Kem dưỡng', 'Centella Asiatica Extract (72 %), Glycerin, Propanediol, Dipropylene Glycol, Cyclomethicone, Water, 1, 2 - Hexanediol, Trehalose, Caprylyl Methicone, C12 - 14 Pareth - 12, Carbomer, Tromethamine, Ammonium Acryloyldimethyltaurate/​VP Copolymer, C30 - 45 Alkyl Cetearyl Dimethicone Crosspolymer, Xanthan Gum, Mentha Piperita Leaf ( Peppermint ) Extract, Zingiber Officinale (Ginger) Root Extract, Butylene Glycol, Ethylhexylglycerin, Dipotassium Glycyrrhizate, Tranexamic Acid, Coptis Chinensis Root Extract, Theobroma Cacao (Cocoa) Extract, Dextrin, Leuconostoc/​Radish Root Ferment Filtrate, Biosaccharide Gum - 1, Disodium EDTA, Sodium Hyaluronate, Beta-Glucan, Ceramide EOP, Ceramide NS, Ceramide NP, Ceramide AP, Phytosphingosine, Hydrogenated Lecithin, Cetearyl Alcohol, Stearic Acid, Cholesterol'),
('Skin1004_Toner','Skin1004','Toner', 'Centella Asiatica Extract, Water, 1,2-Hexanediol, Dipropylene Glycol, Niacinamide, Gluconolactone, Tromethamine, Carbomer, Sodium Citrate, Adenosine, Disodium Edta, Dipotassium Glycyrrhizate, Betaine, Hyaluronic Acid, Ethylhexylglycerin'),
('SkinAqua_KCN','SkinAqua','Kem chống nắng', 'Water, Alcohol, Ethylhexyl Methoxycinnamate, Butylene Glycol, Diphenylsiloxy Phenyl Trimethicone, Titanium Dioxide, Diethylamino Hydroxybenzoyl Hexyl Benzoate, Sodium Hyaluronate, Magnesium Ascorbyl Phosphate, Passiflora Edulis Fruit Extract, Hydrolyzed Prunus Domestica, Rosa Roxburghii Fruit Extract, Bis-PEG-18 Methyl Ether Dimethyl Silane, Methyl Methacrylate Crosspolymer, Glycol Dimethacrylate Crosspolymer, Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine, Acrylates Copolymer, Polysorbate 60, Acrylates/​C10-30 Alkyl Acrylate Crosspolymer, Triethanolamine, Ammonium Acryloyldimethyltaurate/​VP Copolymer, Silica, PEG-12 Dimethicone, Polystyrene, Polyvinyl Alcohol, Disodium EDTA, Xanthan Gum, Alumina, BHT, Polyglyceryl-2 Triisostearate, Synthetic Fluorphlogopite, Tin Oxide, Ci 73360, Ci 42090, Fragrance'),
('Simple_Toner','Simple','Toner', 'Aqua, Hydrogenated Starch Hydrolysate, Sodium PCA, Allantoin, Phenoxyethanol, Disodium EDTA, Propylene Glycol, Cetylpyridinium Chloride, Niacinamide, Hamamelis Virginiana Leaf Water, Panthenol, Decyl Glucoside');
