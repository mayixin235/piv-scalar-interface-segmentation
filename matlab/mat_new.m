%PIV PARTICLE IMAGE GENERATOR
for i = [0:159] %FOR TRAINING IMAGE GENERATION
    image_folder = 'C:\Users\hp\Desktop\diss\matlab\data\case20\train\image raw'
    mask_folder = 'C:\Users\hp\Desktop\diss\matlab\data\case20\train\mask raw'

    background = Im_Generator(); %create background image
    [layer1, layer2, layer3, layer4, layer5, line] = Layer_Generator(); %create layers to add on background image
    layer = layer1 + layer2;
    result = background + layer; %final image
    
    % figure showing the layers
    % figure;
    % imagesc(layer);
    % colormap gray
    % axis equal
    
    %figure showing the final image
    figure;
    q = imagesc(result);
    colormap gray
    % axis image
    set(gca,'XTick',[], 'YTick', []) %get rid of axis values
    set(gca,'LooseInset',get(gca,'TightInset')); %get rid of white space
    
    %save the image as a Portable Graphics Format file(png)into the MatLab
    imgName = [image_folder,'\' num2str(i),'.png'] ;
    saveas(q,imgName);
    
    
    %figure showing the final image with the line
    figure;
    imagesc(result);
    colormap gray
    axis equal
    
    hold on
    Nx=256;
    x=1:1:Nx;
    plot(x,line,'k-', 'Color','#0076a8')
    axis([0 256 0 256]);
    hold off
    
    % create a mask image using roi
    v = [256,256; 0,256; 0,line(1); x', line; 256,256];
    h = drawpolygon('Position',v, 'Color','w');
    
    bw = createMask(h);
    z = imshow(bw);
    %axis equal
    set(gca,'LooseInset',get(gca,'TightInset')); %get rid of white space
    
    %save the image as a Portable Graphics Format file(png)into the MatLab
    maskName = [mask_folder,'\' num2str(i),'.png'] ;
    saveas(z,maskName);
    
end


for i = [160:179] % FOR VALIDATION IMAGE GENERATION
    image_folder = 'C:\Users\hp\Desktop\diss\matlab\data\case20\validation\image raw'
    mask_folder = 'C:\Users\hp\Desktop\diss\matlab\data\case20\validation\mask raw'

    background = Im_Generator(); %create background image
    [layer1, layer2, layer3, layer4, layer5, line] = Layer_Generator(); %create layers to add on background image
    layer = layer1 + layer2;
    result = background + layer; %final image
    
    % figure showing the layers
    % figure;
    % imagesc(layer);
    % colormap gray
    % axis equal
    
    %figure showing the final image
    figure;
    q = imagesc(result);
    colormap gray
    % axis image
    set(gca,'XTick',[], 'YTick', []) %get rid of axis values
    set(gca,'LooseInset',get(gca,'TightInset')); %get rid of white space
    
    %save the image as a Portable Graphics Format file(png)into the MatLab
    imgName = [image_folder,'\' num2str(i),'.png'] ;
    saveas(q,imgName);
    
    
    
    %figure showing the final image with the line
    figure;
    imagesc(result);
    colormap gray
    axis equal
    
    hold on
    Nx=256;
    x=1:1:Nx;
    plot(x,line,'k-', 'Color','#0076a8')
    axis([0 256 0 256]);
    hold off
    
    % create a mask image using roi
    v = [256,256; 0,256; 0,line(1); x', line; 256,256];
    h = drawpolygon('Position',v, 'Color','w');
    
    bw = createMask(h);
    z = imshow(bw);
    %axis equal
    set(gca,'LooseInset',get(gca,'TightInset')); %get rid of white space
    
    %save the image as a Portable Graphics Format file(png)into the MatLab
    maskName = [mask_folder,'\' num2str(i),'.png'] ;
    saveas(z,maskName);
    
end


for i = [180:199] %FOR TESTING IMAGE GENERATION
    image_folder = 'C:\Users\hp\Desktop\diss\matlab\data\case20\test\image raw'
    mask_folder = 'C:\Users\hp\Desktop\diss\matlab\data\case20\test\mask raw'

    background = Im_Generator(); %create background image
    [layer1, layer2, layer3, layer4, layer5, line] = Layer_Generator(); %create layers to add on background image
    layer = layer1 + layer2;
    result = background + layer; %final image
    
    % figure showing the layers
    % figure;
    % imagesc(layer);
    % colormap gray
    % axis equal
    
    %figure showing the final image
    figure;
    q = imagesc(result);
    colormap gray
    % axis image
    set(gca,'XTick',[], 'YTick', []) %get rid of axis values
    set(gca,'LooseInset',get(gca,'TightInset')); %get rid of white space
    
    %save the image as a Portable Graphics Format file(png)into the MatLab
    imgName = [image_folder,'\' num2str(i),'.png'] ;
    saveas(q,imgName);
    
    
    
    %figure showing the final image with the line
    figure;
    imagesc(result);
    colormap gray
    axis equal
    
    hold on
    Nx=256;
    x=1:1:Nx;
    plot(x,line,'k-', 'Color','#0076a8')
    axis([0 256 0 256]);
    hold off
    
    % create a mask image using roi
    v = [256,256; 0,256; 0,line(1); x', line; 256,256];
    h = drawpolygon('Position',v, 'Color','w');
    
    bw = createMask(h);
    z = imshow(bw);
    %axis equal
    set(gca,'LooseInset',get(gca,'TightInset')); %get rid of white space
    
    %save the image as a Portable Graphics Format file(png)into the MatLab
    maskName = [mask_folder,'\' num2str(i),'.png'] ;
    saveas(z,maskName);
    
end

